
def cal_bayes(prior_A, prob_b_dado_A, prob_B):
    return (prior_A * prob_b_dado_A)/ prob_B


if __name__ == "__main__":
    prob_cancer = 1 / 100000
    prob_sintoma_dado_no_cancer = 10 / 99990
    prob_sintoma_dado_cancer = 1
    prob_no_cancer = 1 - prob_cancer

    prob_sintoma = (prob_sintoma_dado_cancer * prob_cancer) + (prob_sintoma_dado_no_cancer * prob_no_cancer)

    prob_cancer_dado_sintoma = cal_bayes(prob_cancer, prob_sintoma_dado_cancer, prob_sintoma)

    print(f'La probabilidad de tener cancer dado que tengo un sintoma es {prob_cancer_dado_sintoma}')