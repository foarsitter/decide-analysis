from decideanalyses import helpers


def test_list_to_sql_param():

    param = helpers.list_to_sql_param([1, 2, 3])

    assert param == "'1','2','3'"


def test_get_all_actors_by_model_run_ids_sql():

    x = helpers.get_all_actors_by_model_run_ids_sql([1, 2, 3])

    print(x)
