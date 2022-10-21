# coding=utf-8
import string
# input: array with multiple strings
# expected output: rank of the 3 most often repeated words in given set of strings and number of times they occured, case insensitive

SENTENCES = [
    'Taki mamy klimat',
    'Wszędzie dobrze ale w domu najlepiej',
    'Wyskoczył jak Filip z konopii',
    'Gdzie kucharek sześć tam nie ma co jeść',
    'Nie ma to jak w domu',
    'Konduktorze łaskawy zabierz nas do Warszawy',
    'Jeżeli nie zjesz obiadu to nie dostaniesz deseru',
    'Bez pracy nie ma kołaczy',
    'Kto sieje wiatr ten zbiera burzę',
    'Być szybkim jak wiatr',
    'Kopać pod kimś dołki',
    'Gdzie raki zimują',
    'Gdzie pieprz rośnie',
    'Swoją drogą to gdzie rośnie pieprz?',
    'Mam nadzieję, że poradzisz sobie z tym zadaniem bez problemu',
    'Nie powinno sprawić żadnego problemu, bo Google jest dozwolony',
]

# Example result:
# 1. "mam" - 12
# 2. "tak" - 5
# 3. "z" - 2

# Good luck! You can write all the code in this file.


def count_words(sentences):
    words = ' '.join(sentences).lower().translate(str.maketrans('', '', string.punctuation))

    results = {}
    for word in words.split():
        if word in results:
            results[word] += 1
        else:
            results[word] = 1
    sorted_results = [(k, v) for k, v in sorted(results.items(), key=lambda item: item[1], reverse=True)]
    return sorted_results


if __name__ == '__main__':
    sorted_results = count_words(SENTENCES)
    print(f"""1. "{sorted_results[0][0]}" - {sorted_results[0][1]}
2. "{sorted_results[1][0]}" - {sorted_results[1][1]}
3. "{sorted_results[2][0]}" - {sorted_results[2][1]}""")


