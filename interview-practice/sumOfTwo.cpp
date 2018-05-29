bool sumOfTwo(std::vector<int> a, std::vector<int> b, int v) {
    std::unordered_map<int, int> dict;
 
    for (size_t i = 0; i < b.size(); i++) {
        dict[b[i]] = 1;
    }
    
    for (size_t j = 0; j < a.size(); j++) {
        if (dict.find((v - a[j])) != dict.end()) {
            return true;
        }
    }
    return false;
}
