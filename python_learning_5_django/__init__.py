import logging

'''
logging settings
'''
logging.basicConfig(
    level=logging.INFO,
    format="%(filename)s [LINE:%(lineno)-10d] # %(levelname)-8s [%(asctime)s] %(message)s"
    # , filename=''
    # , filemode='w'
)
