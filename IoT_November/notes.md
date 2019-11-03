
- Concept of _Event Row Structure_ whereby each row is an event. In the simplest form, each event row contains a sub-activity (the event), a start timestamp and an end timestamp. Additional metadata can be added or removed based on the needs of the analysis. For example, using the start and end timestamps, the duration can be determined (in any temporal units desired). The day and time of day can be determined, the 'phase' of the day can be determined, weekend or weekday ...

- Concept of the _Boolean Array Structure_ whereby each row is a timestamp and the columns of the dataset are the sub activities and values of the cells are boolean to indicate if the sub activity is occuring (1) or is not occuring (0). All metadata associated with the timestamps and then sub activities is stored in separate reference files (e.g. *.csv, *.json).

