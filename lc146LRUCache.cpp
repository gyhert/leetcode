/* We can use stl container list as a double
ended queue to store the cache keys, with
the descending time of reference from front
to back and a set container to check presence
of a key. But to fetch the address of the key
in the list using find(), it takes O(N) time.
	This can be optimized by storing a reference
	(iterator) to each key in a hash map. */
  #include<bits/stdc++.h>
  using namespace std;
  
  class LRUcache
  {
      list<int> dq;
      unordered_map<int, list<int>::iterator> ma;
      int csize;
  public:
    LRUCache(int);
    void refer(int);
    void display();
    };
 /* Refers key x with in the LRU cache */
 void LRUCache::refer(int x)
 {
    if(ma.find(x) == ma.end())
    {
      //not present in cache
      if(dp.size() == csize)
      {
        //cache is full 
        int last = dq.back();
        dq.pop_back();
        ma.erase(last);
        }
    }
    else
        dq.erase(ma[x]);
        dq.push_front(x);
        ma[x] = dq.begin();
 }
 // display contents of cache
 void LRUCache::dispaly()
 {
    for(auto it = dq.begin(); it != dq.end(); it++)
      count <<(*it)<< " ";
    cout << endl;
 
 int main()
 {
      LRUCache ca(4);
      ca.refer(1);
      ca.refer(2);
      ca.refer(3);
      ca.refer(1);
      ca.refer(4);
      ca.refer(5);
      ca.display();
      
      return 0;
      }
 
    
      
