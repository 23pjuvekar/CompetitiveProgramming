#include <vector>
#include <queue>
#include <unordered_map>
#include <algorithm>
using namespace std;


struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};

class Solution {
public:
    vector<int> findMode(TreeNode* root) {
        unordered_map<int, int> node_counter;
        queue<TreeNode*> q;
        q.push(root);
        
        while (!q.empty()) {
            TreeNode* node = q.front();
            q.pop();
            node_counter[node->val]++;
            
            if (node->left) {
                q.push(node->left);
            }
            if (node->right) {
                q.push(node->right);
            }
        }
        
        int curr_mode = 0;
        vector<int> curr_list;
        
        for (const auto& pair : node_counter) {
            int key = pair.first;
            int val = pair.second;
            
            if (val > curr_mode) {
                curr_list = {key};
                curr_mode = val;
            } else if (val == curr_mode) {
                curr_list.push_back(key);
            }
        }
        
        return curr_list;
    }
};