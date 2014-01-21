Class DataTemplate:

    """
    Object is a dataset template that defines key metadata about a dataset file, table, or form record.
    This is the baseclass for a set of child objects that handle specific cases for dataset types, for example,
    a geospatial time-series data set, or a geospatial static set. An instance of this class describes and points
    to a specific dataset or set of datasets
    """

    template_id = ''

    template_name = ''

    created_by = ''

    last_modified_time = ''

    last_modified_by = ''

    template_children = []


