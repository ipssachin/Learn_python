from unit_test import *

# #Linear search in list
#
def search_linear(xs, target):
    """ Find and return the index of target in sequence xs """
    # print(xs,target)

    for (i, v) in enumerate(xs):
        # print(i, v)
        if v == target:
            return i
    return -1
# #
# friends = ["Joe", "Zoe", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]
# test(search_linear(friends, "Zoe") == 1)
# test(search_linear(friends, "Joe") == 0)
# test(search_linear(friends, "Paris") == 6)
# test(search_linear(friends, "Sagar") == -1)
# test(search_linear(friends, "heman") == -1)
#

# #Next exmaple
def find_unknown_words(vocab, wds):
    """ Return a list of words in wds that do not occur in vocab """
    result = []
    for w in wds:
        if (search_linear(vocab, w) < 0):
            result.append(w)
    return result

# vocab = ["apple", "boy", "dog", "down",
#                           "fell", "girl", "grass", "the", "tree"]
book_words = "the apple fell from the tree to the grass".split()
# test(find_unknown_words(vocab, book_words) == ["from", "to"])
# test(find_unknown_words([], book_words) == book_words)
# test(find_unknown_words(vocab, ["the", "boy", "fell","SM"]) != [])
#
# #load vords from file
#
def load_words_from_file(filename):
    """ Read words from filename, return list of words. """
    f = open(filename, "r")
    file_content = f.read()
    f.close()
    wds = file_content.split()
    return wds
#
bigger_vocab = load_words_from_file("vocab.txt")
# print("There are {0} words in the vocab, starting with\n {1} "
#               .format(len(bigger_vocab), bigger_vocab[:106]))
# #
#
# #
def text_to_words(the_text):
    """ return a list of words with all punctuation removed,
        and all in lowercase.

        """
    my_substitutions = the_text.maketrans(
      # If you find any of these
      "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!\"#$%&()*+,-./:;<=>?@[]^_`{|}~'\\",
      # Replace them by these
      "abcdefghijklmnopqrstuvwxyz                                          ")

    # Translate the text now.
    cleaned_text = the_text.translate(my_substitutions)

    wds = cleaned_text.split()

    return wds
#
#
# print(text_to_words('"Well, I never!", said Alice.'))


#
#
#
#
#
# test(text_to_words("My name is Earl!") == ["my", "name", "is", "earl"])
# test(text_to_words('"Well, I never!", said Alice.') ==["well", "i", "never", "said", "alice"])
#
#
#
# #
#
def get_words_in_book(filename):
    """ Read a book from filename, and return a list of its words. """
    f = open(filename, "r")
    content = f.read()
    f.close()
    wds = text_to_words(content)
    return wds

book_words = get_words_in_book("alice_in_wonderland.txt")
# print("There are {0} words in the book, the first 100 are\n{1}".
           # format(len(book_words), book_words[:100]))
#
#
import time

t0 =  time.process_time()
print(t0)
missing_words = find_unknown_words(bigger_vocab, book_words)
t1 = time.process_time()
print("There are {0} unknown words.".format(len(missing_words)))
print("That took {0:.4f} seconds.".format(t1-t0))

# missing_words = find_unknown_words(bigger_vocab, book_words)

#
# # #binary search
# def search_binary(xs, target):
#     """ Find and return the index of key in sequence xs """
#     lb = 0
#     ub = len(xs)
#     while True:
#         if lb == ub:   # If region of interest (ROI) becomes empty
#            return -1
#
#         # Next probe should be in the middle of the ROI
#         mid_index = (lb + ub) // 2
#
#         # Fetch the item at that position
#         item_at_mid = xs[mid_index]
#
#         # print("ROI[{0}:{1}](size={2}), probed='{3}', target='{4}'"
#         #       .format(lb, ub, ub-lb, item_at_mid, target))
#
#         # How does the probed item compare to the target?
#         if item_at_mid == target:
#             return mid_index      # Found it!
#         if item_at_mid < target:
#             lb = mid_index + 1    # Use upper half of ROI next time
#         else:
#             ub = mid_index        # Use lower half of ROI next time
#
# xs = [2,3,5,7,11,13,17,23,29,31,37,43,47,53]
# test(search_binary(xs, 20) == -1)
# test(search_binary(xs, 99) == -1)
# test(search_binary(xs, 1) == -1)
# for (i, v) in enumerate(xs):
#     test(search_binary(xs, v) == i)
