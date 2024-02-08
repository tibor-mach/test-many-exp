if __name__ == "__main__":
    import dvc.api
    from dvclive import Live

    params = dvc.api.params_show()
    Live.log_param(params["x"])