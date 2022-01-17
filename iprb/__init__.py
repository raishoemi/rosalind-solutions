def solve():
    k = 26
    m = 30
    n = 25
    total = k + m + n
    # Caclulate homo recessive progeny probabiliy and reduct from 1
    p_both_homo_recessive = (k / total) * ((k - 1) / (total - 1))
    p_homo_recessive_and_hetero = (k / total) * (m / (total - 1)) * 0.5
    p_homo_recessive_and_hetero += (m / total) * (k / (total - 1)) * 0.5
    p_both_hetero = (m / total) * ((m - 1) / (total - 1)) * 0.25
    p_dom_phenotype = 1 - p_both_homo_recessive - p_homo_recessive_and_hetero - p_both_hetero
    print(p_dom_phenotype)
