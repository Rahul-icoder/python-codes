def main():
    def longestWord(value):
        longword = ""
        
        for item in value:
            if len(item)>len(longword):
                longword=item
        print(longword)
    longestWord(["hello","spiderman","peacock","dark knight"])
            
main()
