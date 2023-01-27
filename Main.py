from Params import *
from Read_trans import *
from Merge_data import *
from Clasify_df import *


def run():
    # call params
    params_m = params()

    # read the file & and transform goal with damage
    read_m = read_trans(params_m.Website_Goals_Supermetrics_Update)
    file_m = read_m.read_transf()
    # print (file_m)

    Clasify_m = read_clasify(params_m.Website_Goals_Supermetrics_Update)

    filecls_2_m1 = Clasify_m.read_clsify("view")
    filecls_2_m2 = Clasify_m.read_clsify("viewName")
    list_goalname = Clasify_m.read_clsify("goalname")

    list_view = Clasify_m.clean(filecls_2_m1)
    list_viewName = Clasify_m.clean(filecls_2_m2)

    merge_m = merge(file_m, list_view, list_viewName, list_goalname)

    df_fn = merge_m.merge_data()

    df_fn.to_csv(
        "C:\\Users\\Santiago\\Documents\\GitHub\\Web_site_goal_final_version\\output\\hello.csv",
        index=False,
    )
    # print(list_view)
    # print(list_viewName)
    # print(list_goalname)

    # print(z = 'viewName')

    # extract and fix goals with problems

    # fix_maingl = Fix_Goals(file_m, params_m.regex)

    # match_m = fix_maingl.match_goals()


if __name__ == "__main__":
    run()
