def group_words_by_length(input_file):
    word_length_dict = {}

    with open(input_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            words = line.split()
            
            for word in words:
                cleaned_word = word.replace('.', '').replace(',', '')                                
                
                word_length = len(cleaned_word)
                
               
                if word_length not in word_length_dict:
                    word_length_dict[word_length] = []
                word_length_dict[word_length].append(cleaned_word)
    
   
    for length, words in word_length_dict.items():
        output_file = f"{length}.txt"
        with open(output_file, 'w') as file:
            for word in words:
                file.write(word + '\n')  

    print("Processing is completed")

input_file = 'lorem.txt'

# Process the file
group_words_by_length(input_file)







            
           
