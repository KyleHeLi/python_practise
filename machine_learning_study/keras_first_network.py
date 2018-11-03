#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from keras.models import Sequential
from keras.layers import Dense

import logging
import numpy as np

# create logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# create file handler
log_file = "./nn_study.log"
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)

# create formatter
fmt = "%(asctime)-15s %(levelname)s %(filename)s %(lineno)d %(process)d %(message)s"
datefmt = "%a %d %b %Y %H:%M:%S"
formatter = logging.Formatter(fmt, datefmt)

# add handler and formatter to logger
fh.setFormatter(formatter)
logger.addHandler(fh)


def main():
    enter = "\r\n"
    contentCut = "================================"

    # fix random seed for reproducibility
    logger.info("choose a random seed")
    np.random.seed(7)
    # load pima indians dataset
    logger.info("load data")
    dataset = np.loadtxt("data/pima-indians-diabetes.csv", delimiter=",")
    # split into input (X) and output (Y) variables
    X = dataset[:, 0:8]
    Y = dataset[:, 8]
    logger.debug("X values: %s %s %s %s" % (enter, X, enter, contentCut))
    logger.debug("Y values: %s %s %s %s" % (enter, Y, enter, contentCut))

    # create model
    logger.info("create the model")
    model = Sequential()
    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    # compile model
    logger.info("compile the model")
    model.compile(loss='binary_crossentropy',
                  optimizer='adam',
                  metrics=['accuracy'])

    # fit the model
    logger.info("fit the model")
    model.fit(X, Y, epochs=150, batch_size=10, verbose=2)

    # evaluate the model
    logger.info("evaluate the model")
    scores = model.evaluate(X, Y)
    logger.debug("\n%s: %.2f%%" % (model.metrics_names[1], scores[1] * 100))

    # calculate predictions
    logger.info("calculate predictions")
    predictions = model.predict(X)
    logger.debug("Predictions: %s" % predictions)

    # round predictions
    rounded = [round(x[0]) for in predictions]
    logger.debug("round predictions: %s", rounded)


if __name__ == '__main__':
    main()
