=begin
1.4 Palindrome Permutation: Given as string, write a function to check if it is
    a permutation of a palindrome. The palindrome does not need to be limited
    to just dictionary words. 

    EXAMPLE:
    input = Tact Coa
    output = True 
    There exist permutation of the string 'tactcoa' that are palidromes (i.e. 'tacocat')
=end

# This is an implementation of Is Palindrome in Ruby

# Let's think about what qualifies a string as a palindrome permutation:
# Each value must have a pair exempting one if the length of the list is odd.

# Let's create a hash of possible inputs.
inputs = {
    0 => "Rochester",
    1 => "soh cah toa",
    2 => "Tact Coa",
    3 => "Level"
}

def check_palindrome_permute(str_input)
    # Checks if a given string or list is a permutation of a palindrome
    # To have a robust function that can handle spaces and capitalization,
    # let's strip whitespace from the input and set all letters to 
    # lower case. I'm going to include punctuation as possible values 
    # used in the palindrome.
    # We change the string to an array in order to make it easily checkable
    str_input = str_input.gsub(/\s+/, "").downcase.split(//)
    # Now, to find the unique chars in string we need to apply the uniq method. 
    letters = str_input.uniq
    # If the number of values in str_input is even, it is allowed zero unpaired chars
    unpaired_allowed = 0
    if str_input.length%2 != 0
        # If str_input has an odd number of values, it can have one unpaired char.
        unpaired_allowed = 1
    end
    # We go through the characters that are in the input. If there is an unpaired char
    # we reduce unpaired_allowed. If it goes below zero, the input is not a
    # permutation of a palindrome.
    for i in 0..letters.length
        if str_input.count(letters[i]) % 2 != 0
            unpaired_allowed -= 1
            if unpaired_allowed < 0
                return false
            end
        end
    end
    return true
end

for i in 0..inputs.length-1
    puts "#{inputs[i]} is a palindrome permutation: #{check_palindrome_permute(inputs[i])}"
end