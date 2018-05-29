bool containsDuplicates(std::vector<int> a) {
    std::unordered_map<int, int> tbl;
    
    size_t count = a.size();
    if (!count)
        return false;
    
    for (size_t i = 0; i < count; i++) {
        if (tbl.count(a[i]) > 0) {
            return true;
        }
        tbl[a[i]] = 1;
    }
    
    return false;
}
