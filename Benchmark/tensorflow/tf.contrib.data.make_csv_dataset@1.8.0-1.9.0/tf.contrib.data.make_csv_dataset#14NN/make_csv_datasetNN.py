import tensorflow as tf
tf.contrib.data.make_csv_dataset('dev.csv',  1,  None,  None,  None,  ',',  True, na_value='', header=True, comment=None, num_epochs=None, shuffle=True, shuffle_buffer_size=1, shuffle_seed=None, prefetch_buffer_size=1, num_parallel_reads=1, num_parallel_parser_calls=2, sloppy=False, default_float_type=tf.float32, num_rows_for_inference=1)
