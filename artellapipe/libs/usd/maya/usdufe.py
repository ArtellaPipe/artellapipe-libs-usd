import logging

import ufe

LOGGER = logging.getLogger('artellapipe-libs-usd')


def is_ufe_usd_path(ufe_object):
    segment_count = len(ufe_object.path().segments)
    if segment_count < 2:
        return False


def get_ufe_selection():
    try:
        return next(iter(ufe.GlobalSelection.get()))
    except Exception:
        return None


def get_dag_and_prim_from_ufe(ufe_object):
    if ufe_object is None:
        return None, None

    segment_count = len(ufe_object.path().segments)
    if segment_count == 0:
        return None, None

    dag_path = str(ufe_object.path().segments[0])[6:]
    if segment_count == 1:
        return dag_path, None

    prim_path = str(ufe_object.path().segments[1])

    return dag_path, prim_path


def get_selected_dag_and_prim():
    return get_dag_and_prim_from_ufe(get_ufe_selection())


def parent_selection():
    ufe_selection = iter(ufe.GlobalSelection.get())
    ufe_selection_list = [ufe_item for ufe_item in ufe_selection]

    # Clear this selection so nobody will try to use it
    # next steps can result in new selection being made due to potential call to create_access_plug
    ufe_selection = None

    if len(ufe_selection) < 2:
        LOGGER.warning('Select at least two objects .DAG child/ren and USD parente at the end')
        return

    ufe_parent = ufe_selection_list[-1]
    ufe_children = ufe_selection_list[:-1]

    parent_items(ufe_children, ufe_parent)


def parent_items(ufe_children, ufe_parent):
    if not is_ufe_usd_path(ufe_parent):
        LOGGER.warning('Last select item needs to be USD parent')
        return

    parent_dag_path, parent_usd_prim_path = get_dag_and_prim_from_ufe(ufe_parent)
