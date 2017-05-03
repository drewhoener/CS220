from PyQt5.QtGui import QStandardItemModel, QStandardItem


def get_table_report(result_set):
    """ the result set from the database is converted to a form that can be rendered by the view class."""
    list_res = convert_to_lists(result_set)
    model = QStandardItemModel()
    # the first row contains the column headers (can not use them and use more user-friendly names)
    model.setHorizontalHeaderLabels(list_res[0])
    res_rows = list_res[1:]
    for row in res_rows:
        model.appendRow(get_items_row(row))
    return model


def get_items_row(result_row):
    """ set the values from the result set into a new row in the model format"""
    item_row = []
    for val in result_row:
        item = QStandardItem(val)
        item.setEditable(False)
        item_row.append(item)
    return item_row


def convert_to_lists(res_set):
    """ res is a list of tuples- convert to list of lists for rendering. also cast all numbers to string """
    return [list(map(str, elem)) for elem in res_set]
