tree = {
    'age': 80,
    'children': [
        {
            'age': 55,
            'children': [
                {
                    'age': 32,
                    'children': [
                        {
                            'age': 5,
                            'children': []
                        }
                    ]
                }
            ]
        },
        {
            'age': 52,
            'children': [
                {
                    'age': 22,
                    'children': []
                },
                {
                    'age': 24,
                    'children': []
                }
            ]
        },
        {
            'age': 50,
            'children': []
        }
    ]
}


def youngest(tree):
    yougest_age = tree['age']
    for child in tree['children']:
        youngest_in_subtree = youngest(child)
        if yougest_age > youngest_in_subtree:
            yougest_age = youngest_in_subtree

    return yougest_age


print(youngest(tree))
