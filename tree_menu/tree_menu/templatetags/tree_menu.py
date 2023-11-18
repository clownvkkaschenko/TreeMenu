from typing import Dict, List, Optional

from django import template

from tree_menu.models import MenuItem

register = template.Library()


@register.inclusion_tag('templatetags/menu.html', takes_context=True)
def draw_menu(context, menu_title):
    """Шаблонный тег для древовидного меню.

    Извлекает из контекста текущий URL.
    Получает список всех элементов меню для заданного названия.
    Строит древовидное представление меню с помощью функции
    build_menu_tree и передаёт его в шаблон.
    """

    current_url = context['request'].path[1:-1]
    menu_items = MenuItem.objects.filter(
        main_menu__name=menu_title)

    menu_tree = build_menu_tree(list(menu_items), current_url)

    return {'menu_tree': menu_tree}


def build_menu_tree(
        menu_items: List[MenuItem],
        current_url: str,
        parent: Optional[MenuItem] = None
) -> List[Dict[str, object]]:
    """Рекурсивно строит древовидное меню из заданных элементов.

    Эта функция перебирает список элементов меню и строит из них
    иерархическое дерево.
    Рекурсивно вызывается build_menu_tree, что-бы построить список
    дочерних элементов(children) для каждого элемента(item).
    """

    tree = list()
    for item in menu_items:
        if item.parent == parent:
            children = build_menu_tree(menu_items, current_url, parent=item)

            is_active = item.url == current_url
            is_active_children = any(child['active'] for child in children)
            tree.append({
                'item': item,
                'children': children,
                'active': is_active or is_active_children,
                'open': is_active or is_active_children,
            })
    return tree
