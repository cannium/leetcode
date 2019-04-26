struct Node {
    Node* nexts[26] = {nullptr};
    bool end;
};

class StreamChecker {
private:
    Node root;
    string buf;
    
    void extend(Node& node, string& s, int i) {
        if (i < 0) {
            node.end = true;
            return;
        }
        char c = s[i];
        if (node.nexts[c-'a'] == nullptr) {
            Node* n = new Node();
            node.nexts[c-'a'] = n;
            extend(*n, s, i-1);
        } else {
            extend(*(node.nexts[c-'a']), s, i-1);
        }
    }
public:
    StreamChecker(vector<string>& words) {
        for(string s: words) {
            extend(root, s, s.length()-1);
        }
    }
    bool query(char letter) {
        buf += letter;
        auto cur = &root;
        for(int i = buf.size()-1; i >=0; i--) {
            char c = buf[i];
            if (cur->nexts[c-'a'] != nullptr) {
                cur = cur->nexts[c-'a'];
                if (cur->end) {
                    return true;
                }
            } else {
                return false;
            }
        }
        return false;
    }
};

/**
 * Your StreamChecker object will be instantiated and called as such:
 * StreamChecker* obj = new StreamChecker(words);
 * bool param_1 = obj->query(letter);
 */
