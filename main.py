def main():
    path = "books/frankenstein.txt"
    with open(path) as f:
        q = f.read()
        wc = count_words(q)
        cc = count_all_chars(q)
        print_report(path, wc, cc)

def count_words(m):
    g = m.split()
    return len(g)

def count_chars(m, c):
    #m input string
    #c char to search and count
    h = c.lower()
    q = m.count(h)
    return q

def count_all_chars(q):
    counts = {}
    string = list(q)

    for c in string:
        if c.isprintable() and c.isalpha():
            n = c.lower()
            counts[n] = counts.get(n, 0) + 1
    return counts

def sort_on(dict):
    return dict["count"]

def sort_by_value(d):
    sort_list = []
    for k, v in d.items():
        sort_list.append({"letter": k, "count": v})
    sort_list.sort(reverse=True, key=sort_on)
    return sort_list


def print_report(path, word_count, char_count):
    sorted_chars = sort_by_value(char_count)

    print(f"--- Begin report of {path} ---")
    print (f"{word_count} words found in the document\n")

    for n in sorted_chars:
        
        print(f"The '{n['letter']}' character was found {n['count']} times")
        
    print("\n--- End report ---")

main()
