class Evaluator:     
    def zip_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words):
            return (-1)
        for x in range(len(coefs)):
            if not isinstance(coefs[x], (int, float)) or not isinstance(words[x], str):
                return (-1)
        tup = list(zip(coefs, words))
        suma = 0
        for x in tup:
            suma += len(x[1]) * x[0]
        return (suma)

    def enumerate_evaluate(coefs, words):
        if not isinstance(coefs, list) or not isinstance(words, list) or len(coefs) != len(words):
            return (-1)
        for x in range(len(coefs)):
            if not isinstance(coefs[x], (int, float)) or not isinstance(words[x], str):
                return (-1)
        suma = 0
        tup = enumerate(words)
        for x, word in tup:
            suma += len(word) * coefs[x]
        return (suma)

if __name__ == "__main__":
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    
    words = ["Le", 1, "Ipsum", "est", "simple"]
    coefs = [1.0, "2.0", 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))
    
    
    words = ["Le", "Ipsum", "est", "simple"]
    coefs = [1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))