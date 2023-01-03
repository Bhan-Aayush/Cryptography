#Part 1: The Grid Transpose Cryptosystem  

def grid_encrypt(k: int, plaintext: str) -> str:  
    """Encrypt the given plaintext using the grid cryptosystem."""  

    return grid_to_ciphertext(plaintext_to_grid(k, plaintext))  
  
  
def grid_decrypt(k: int, ciphertext: str) -> str:  
    """Decrypt the given ciphertext using the grid cryptosystem.  """
    
    return grid_to_plaintext(ciphertext_to_grid(k, ciphertext))  
  
  
def plaintext_to_grid(k: int, plaintext: str) -> list[list[str]]:  
    """Return the grid with k columns from the given plaintext."""  
   
  split_text = list(plaintext)  
    final_grid = []  
    for i in range(int(len(plaintext) / k)):  
        lst = []  
        for j in range(0 + i * k, k + i * k):  
            lst.extend(split_text[j])  
        list.append(final_grid, lst)  
    return final_grid  
  
  
def grid_to_ciphertext(grid: list[list[str]]) -> str:  
    """Return the ciphertext corresponding to the given grid. """
    
    final_str = ""  
    for i in range(0, len(grid[0])):  
        for item in grid:  
            final_str += item[i]  
    return final_str  
  
  
def ciphertext_to_grid(k: int, ciphertext: str) -> list[list[str]]:  
    """Return the grid corresponding to the given ciphertext."""  
    
    final_grid = []  
    div = int(len(ciphertext) / k)  
    for i in range(div):  
        lst = []  
        for j in range(k):  
            lst.extend(ciphertext[(j * div + i) % len(ciphertext)])  
        list.append(final_grid, lst)  
    return final_grid  
  
  
def grid_to_plaintext(grid: list[list[str]]) -> str:  
    """Return the plaintext message corresponding to the given grid."""  
    
    final_str = ""  
    for item in grid:  
        for i in range(0, len(grid[0])):  
            final_str += item[i]  
    return final_str  
  
  

# Part 3: Breaking The Grid Transpose Cryptosystem  

def grid_break(ciphertext: str, candidates: set[str]) -> set[int]:  
    """Return the set of possible secret keys that decrypt the given ciphertext into a message 
    that contains at least one of the candidate words. 
    """  
    # First step: finds all divisors of the length of ciphertext
    
    divisor_lst = []  
    for i in range(1, len(ciphertext)):  
        if len(ciphertext) % i == 0:  
            divisor_lst.append(i)  
    
    # Second step: Decoding 
    
    lst = []  
    for word in candidates:  
        for char in word:  
            # Creates a list of all possible indexes to check only those for possible words  
            possible_indexes = [c for c in range(len(ciphertext)) if char == ciphertext[c]]  
            lst.extend(check_possible_indexes(word, divisor_lst, ciphertext, possible_indexes))  
    final_set = set(lst)  
    return final_set  
  
  
def check_possible_indexes(w: str, div_list: list[int], ct: str, possible_i: list[int]) -> list[int]:  
    """Helper function to check every possible index"""  
    
    val_list = []  
    for p in possible_i:  
        for div in div_list:  
          
            # Creates every possible word starting from possible indexes  
            word_to_check = [ct[(p + (div * n)) % len(ct)] for n  
                             in range(0, len(w))]  
            split_word = list(w)  
            
            # Compares split candidate word to the possible word being checked  
            if split_word == word_to_check:  
                val_list.append(int(len(ct) / len(w)))  
    return val_list  
  
  
def run_example_break(ciphertext_file: str, candidates: set[str]) -> list[str]:  
    """Return a list of possible plaintexts for the ciphertext found in the given file."""
    
    with open(ciphertext_file, encoding='utf-8') as f:  
        ciphertext = f.read()  
  
    return [ciphertext] + list(candidates)  
  
  

# Part 3: The Permuted Grid Transpose Cryptosystem  
 
def permutation_grid_encrypt(k: int, perm: list[int], plaintext: str) -> str:  
    """Encrypt the given plaintext using the grid cryptosystem."""

    return grid_to_ciphertext(permute_grid(plaintext_to_grid(k, plaintext), perm))  
  
  
def permutation_grid_decrypt(k: int, perm: list[int], ciphertext: str) -> str:  
    """Return the grid corresponding to the given ciphertext."""
    
    return grid_to_plaintext(un_permute_grid(ciphertext_to_grid(k, ciphertext), perm))  
  
  
def permute_grid(grid: list[list[str]], perm: list[int]) -> list[list[str]]:  
    """Return the grid with k columns from the given plaintext."""  
  
    final_grid = []  
  
    for lst in grid:  
        i = 0  
        row = []  
        for _ in range(len(grid[0])):  
            row.append('')  
        for char in lst:  
            y = perm[i]  
            row[y] = char  
            i += 1  
        final_grid.append(row)  
    return final_grid  
  
  
def un_permute_grid(grid: list[list[str]], perm: list[int]) -> list[list[str]]:  
    """Return the grid with k columns from the given plaintext. """ 
    
    final_grid = []  
    row = []  
    for lst in grid:  
        for p in perm:  
            row.append(lst[p])  
        final_grid.append(row)  
        row = []  
    return final_grid  
