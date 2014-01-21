Class DataTemplate:

    """
    Object is a dataset template that defines key metadata about a dataset file, table, or form record.
    This is the baseclass for a set of child objects that handle specific cases for dataset types, for example,
    a geospatial time-series data set, or a geospatial static set. An instance of this class describes and points
    to a specific dataset or set of datasets
    """

    id = ''

    title = ''

    created_by = ''

    last_modified_by = ''

    last_modified_time = ''

    """list of objects"""
    fields = []

    time_effective_start = ''

    time_eff_end = ''

    def set_id():
        """
        a unique identifier. will be _id in mongo. Could use BSON object id

        get from post
        get from cookie
        get from db

        """


    def set_title():
        """
        set by user
        """
