
# Q17: Operator Precedence and Expression Evaluation

expressions = [
    "2 + 3 * 4 ** 2 // 5 - 1",
    "(2 + 3) * 4 ** (2 // 5) - 1",
    "10 - 4 - 2",
    "2 ** 3 ** 2",
    "not True and False or True"
]

predicted = [
    10,
    4,
    4,
    512,
    True
]

actual = [
    2 + 3 * 4 ** 2 // 5 - 1,
    (2 + 3) * 4 ** (2 // 5) - 1,
    10 - 4 - 2,
    2 ** 3 ** 2,
    not True and False or True
]

rules = [
    "** first, then * and //, then + and -",
    "Parentheses first, then **, then * and -",
    "- is evaluated left-to-right",
    "** is evaluated right-to-left",
    "not, then and, then or"
]

print("Q17: Operator Precedence and Expression Evaluation")
print("-" * 100)
print(f"{'Expression':45} {'Predicted':10} {'Actual':10} {'Rule Applied'}")
print("-" * 100)

for exp, pred, act, rule in zip(expressions, predicted, actual, rules):
    print(f"{exp:45} {str(pred):10} {str(act):10} {rule}")
