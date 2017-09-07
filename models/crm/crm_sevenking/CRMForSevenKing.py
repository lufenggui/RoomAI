import algorithms
import tensorflow as tf

class SevenKingCRMPlayer(algorithms.CRMPlayer):
    """
    """

    def cnn_card_variable(self, card_variables):
        cnn_w1 = tf.Variable(tf.float32, (1, 5, 4, 5))
        cnn_w2 = tf.Variable(tf.float32, (1, 5, 4, 5))

        conv1  = tf.nn.conv2d(card_variables, cnn_w1, [1,1,1,1], padding="VALID")
        pool1  = tf.nn.max_pool(conv1, [1,2,2,1],[1,1,1,1],padding="VALID")

        conv2  = tf.nn.conv2d(card_variables, cnn_w1, [1,1,1,1], padding="VALID")
        pool2  = tf.nn.max_pool(conv1, [1,2,2,1],[1,1,1,1],padding="VALID")


    def __init__(self, num_players=2):
        """

        Args:
            num_players:
        """

        self.graph       = tf.Graph()
        self.num_players = num_players

        with self.graph.as_default() as graph:

            self.card_variable       = tf.placeholder(tf.float32, [None,3, 15, 5], "card_variable")
            self.state_action_vector = self.cnn_card_variable(self.card_variable)


            self.handcards_conv1 = tf.nn.conv2d(self.handcards_variables, self.handcards_w["conv_w1"], [1, 1, 1, 1],
                                            padding="VALID")
            self.handcards_pool1 = tf.nn.max_pool(self.handcards_conv1, [1, 2, 2, 1], [1, 1, 1, 1], padding="VALID")
            self.handcards_conv2 = tf.nn.conv2d(self.handcards_pool1, self.handcards_w["conv_w2"], [1, 1, 1, 1],
                                            padding="VALID")
            self.handcards_pool2 = tf.nn.max_pool(self.handcards_conv2, [1, 2, 2, 1], [1, 1, 1, 1], padding="VALID")
            self.handcards_vector = tf.nn.relu(self.handcards_pool1.reshape())


            ### output ####
            self.total_w1    = tf.Variable(tf.float32, [158, 100])
            self.total_bias1 = tf.Variable(tf.float32, [100])
            self.total_w2    = tf.Variable(tf.float32, [158, 1])
            self.total_bias2 = tf.Variable(tf.float32, [1])

            self.total_vector = tf.concat(1, [self.chips_vector, self.bets_vector, self.handcards_vector,
                                          self.opponent_handcards_vector])
            self.output1 = tf.nn.tanh(
                tf.add(tf.matmul(self.total_vector, self.total_w1), self.total_bias1)
            )
            self.output2 = tf.add(tf.matmul(self.output1, self.total_w2), self.total_bias2)

            ### init ###

            self.init = tf.global_variables_initializer()
            self.sess = tf.Session()
            self.sess.run(self.init)

    # @take a action
    def take_action(self):
        """

        """
        pass


    def reset(self):
        """

        """
        pass

    # @receive_info
    def receive_info(self, info):
        """

        Args:
            info:

        Returns:

        """
        pu = info.public_state
        pe = info.person_state

        if pu.turn != pe.id:    return

        floor_bet = pu.floor_bet
        self.chips = np.asarray(pu.chips) / floor_bet
        self.bets = np.asarray(pu.bets) / floor_bet

        self.hand_cards = parseCards(pu, pe.id).reshape([1, 13, 4, 1])
        self.opponent_hand_cards = []
        for i in xrange(pu.num_players):
            if i != pe.id:
                self.opponent_hand_cards.append(parseCards(pu, i))
        self.opponent_hand_cards = np.asarray(self.opponent_hand_cards).reshape([1, 13, 4, pu.num_players])

    def __del__(self):
        """

        """
        self.sess.close()

    def gen_state(self,info):
        """

        Args:
            info:
        """
        raise NotImplementedError("")
    def update_strategies(self, state, actions, targets):
        """

        Args:
            state:
            actions:
            targets:
        """
        raise NotImplementedError("")
    def get_strategies(self, state, actions):
        """

        Args:
            state:
            actions:
        """
        raise NotImplementedError("")
    def update_regrets(self, state, actions, targets):
        """

        Args:
            state:
            actions:
            targets:
        """
        raise NotImplementedError("")
    def get_regrets(self, state, actions):
        """

        Args:
            state:
            actions:
        """
        raise NotImplementedError("")