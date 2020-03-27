'''
NumPy printing exercise for Lab 6, Exercise 6.3
CS-232, Prof. Vander Linden, Calvin University
Completed by Nathan Meyer (tnm6)
@date 27mar2020
'''

from keras.datasets import boston_housing

(train_examples, train_labels), (test_examples,
                                 test_labels) = boston_housing.load_data()

print(
    'training examples \
        \n\tnumber of examples: {} \
        \n\trank: {} \
        \n\tshape: {} \
        \n\tdata type: {}\n\n'.format(
        len(train_examples),
        train_labels.ndim,
        train_labels.shape,
        train_labels.dtype
    ),
    'testing examples \
        \n\tnumber of examples: {} \
        \n\trank: {} \
        \n\tshape: {} \
        \n\tdata type: {}'.format(
        len(test_examples),
        test_labels.ndim,
        test_labels.shape,
        test_labels.dtype
    )
)
