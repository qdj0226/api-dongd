__author__ = "dongd"

if __name__ == '__main__':
    import coreClass
    from config.casSetConfig import RUN
    from src.commonClass.fileDrive import file_sorting_time_latest,file_sorting_time_latest_old,max_filenumber
    from config.configFile import testportsconfig

    if isinstance(RUN, list) and RUN is not None:
        import multiprocessing
        conunt = 0
        for i in RUN:
            projectname = i.split("\\")[-1]
            thread = multiprocessing.Process(target=coreClass.runner, args=(i,projectname))
            thread.start()
        list = file_sorting_time_latest(testportsconfig)
        coreClass.send_email(list, RUN)
        max_filenumber(file_sorting_time_latest_old(testportsconfig), 5, testportsconfig)
    else:
        print("项目只能以列表的形式传入")