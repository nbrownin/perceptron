# Nick Browning
# Neural Network Program

# global variables
learn_rate = .9


def convert_file(f_name):  # converts training data and input files to usable format
    file = ['#'] + list(open(f_name, 'r').read().replace('\n', ''))
    for x in range(len(file)):
        file[x] = 1 if file[x] == '#' else -1
    return file


class CharacterClassifier:
    def __init__(self, rate, l):
        self.learn_rate = rate
        self.training_list = l
        self.weights_list = [1 for x in range(64)]
        self.training_label = [1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
        self.train_model()

    def calculate_sum(self, t_list, w_list):
        return sum([x * y for x, y in zip(t_list, w_list)])

    def update_weights(self, ptr):
        for x in range(len(self.weights_list)):
            self.weights_list[x] = self.weights_list[x] + self.learn_rate * self.training_label[ptr] * \
                                   self.training_list[ptr][x]

    def train_model(self):
        while True:
            stop_training = True
            for y in range(len(self.training_list)):
                # calculate sum
                sum_val = self.calculate_sum(self.training_list[y], self.weights_list)
                # activation function
                sum_val = 1 if sum_val > 0 else -1
                # compare to label, if not equal update weights
                if sum_val != self.training_label[y]:
                    self.update_weights(y)
                    stop_training = False
            if stop_training:
                break

    def evaluate_example(self, filename):
        return 1 if self.calculate_sum(convert_file(filename), self.weights_list) > 0 else -1


if __name__ == "__main__":
    # model setup
    letters = ['A', 'B', 'C', 'D']
    a_list = [convert_file('training_a_1.txt'),
              convert_file('training_a_2.txt'),
              convert_file('training_a_3.txt')]

    b_list = [convert_file('training_b_1.txt'),
              convert_file('training_b_2.txt'),
              convert_file('training_b_3.txt')]

    c_list = [convert_file('training_c_1.txt'),
              convert_file('training_c_2.txt'),
              convert_file('training_c_3.txt')]

    d_list = [convert_file('training_d_1.txt'),
              convert_file('training_d_2.txt'),
              convert_file('training_d_3.txt')]
    a_classifier = CharacterClassifier(learn_rate, a_list + b_list + c_list + d_list)
    b_classifier = CharacterClassifier(learn_rate, b_list + a_list + c_list + d_list)
    c_classifier = CharacterClassifier(learn_rate, c_list + a_list + b_list + d_list)
    d_classifier = CharacterClassifier(learn_rate, d_list + a_list + b_list + c_list)

    while True:  # evaluation loop
        i = input('Please enter a filename or type q to quit:')
        if i.lower() == 'q':
            break
        try:
            results = [a_classifier.evaluate_example(i), b_classifier.evaluate_example(i),
                       c_classifier.evaluate_example(i), d_classifier.evaluate_example(i)]
            if 1 in results:
                print('This letter looks like:')
                print(' + '.join([letters[x] for x in range(len(results)) if results[x] == 1]))
            else:
                print('Letter does not look like A, B, C, or D.')
        except:
            print('Filename error, try again!')

print('\nDone')
