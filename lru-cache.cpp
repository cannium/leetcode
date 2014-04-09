#include<iostream>
#include<map>
using namespace std;

class LRUCache{
public:
    struct triple
    {
        int olderKey;
        int youngerKey;
        int value;
    };
    int capacity;
    map<int, triple> cache;
    int oldestKey;
    int youngestKey;


    LRUCache(int capacity) {
        this -> capacity = capacity;
        cache.clear();
    }
    
    int get(int key) {
        if(cache.count(key) > 0)
        {
            if(key != youngestKey)
            {
                if(key == oldestKey)
                {
                    oldestKey = cache[key].youngerKey;
                    cache[oldestKey].olderKey = -1;

                    cache[key].olderKey = youngestKey;
                    cache[key].youngerKey = -1;

                    cache[youngestKey].youngerKey = key;

                    youngestKey = key;
                }
                else
                {
                    cache[cache[key].youngerKey].olderKey = cache[key].olderKey;
                    cache[cache[key].olderKey].youngerKey = cache[key].youngerKey;

                    cache[key].olderKey = youngestKey;
                    cache[key].youngerKey = -1;
                    
                    cache[youngestKey].youngerKey = key;
                    youngestKey = key;
                }
            }
            return cache[key].value;
        }
        return -1;
    }
    
    void set(int key, int value) {
        if(cache.empty())
        {
            youngestKey = key;
            oldestKey = key;
            cache[key].value = value;
            cache[key].youngerKey = -1;
            cache[key].olderKey = -1;
            return;
        }
        if(get(key) != -1)
        {
            cache[key].value = value;
        }
        else
        {
            cache[key].value = value;
            cache[key].olderKey = youngestKey;
            cache[key].youngerKey = -1;
            cache[youngestKey].youngerKey = key;
            youngestKey = key;
            if(cache.size() > capacity)
            {
                oldestKey = cache[oldestKey].youngerKey;
                cache.erase(cache[oldestKey].olderKey);
            }
        }
    }

};


int main()
{
    /*
    LRUCache cache(2);
    cache.set(2,1);
    cache.set(1,1);
    cout << cache.get(2) << endl;
    cache.set(4,1);
    cout << cache.get(1) << endl;
    cout << cache.get(2) << endl;
    */
    /*
    LRUCache cache(1);
    cache.set(2,1);
    cout << cache.get(2) << endl;
    */
    LRUCache cache(2);
    cout << cache.get(2) << endl;
    cache.set(2,6);
    cout << cache.get(1) << endl;
    cache.set(1,5);
    cache.set(1,2);
    cout << cache.get(1) << endl;
    cout << cache.get(2) << endl;
}
