/*
    @author:        yusuufaslan
    @date:          06.06.2023
    @problem:       895. Maximum Frequency Stack
*/


class FreqStack {
public:
    unordered_map<int, int> frequencies;
    unordered_map<int, stack<int>> hash;
    int maxFrequency;

    FreqStack() {
        maxFrequency = 0;
    }
    
    void push(int val) {
        maxFrequency = max(maxFrequency, ++frequencies[val]);
        hash[frequencies[val]].push(val);
    }
    
    int pop() {
        int val = hash[maxFrequency].top();
        hash[maxFrequency].pop();

        if (!hash[frequencies[val]].size())
            maxFrequency--;

        frequencies[val]--;
        
        return val;
    }
};

/**
 * Your FreqStack object will be instantiated and called as such:
 * FreqStack* obj = new FreqStack();
 * obj->push(val);
 * int param_2 = obj->pop();
 */

/*
Problem Description:
Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.

*/