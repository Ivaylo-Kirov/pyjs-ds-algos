/**
 * Initialize your data structure here.
 */
var MyHashMap = function() {
    this.items = new Array();
    for (let i = 0; i < 100000; ++i) {
        this.items.push(-1);
    }
    //items.fill(-1);
};

/**
 * value will always be non-negative. 
 * @param {number} key 
 * @param {number} value
 * @return {void}
 */
MyHashMap.prototype.put = function(key, value) {
    this.items[key] = value;
};

/**
 * Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key 
 * @param {number} key
 * @return {number}
 */
MyHashMap.prototype.get = function(key) {
    return this.items[key];
};

/**
 * Removes the mapping of the specified value key if this map contains a mapping for the key 
 * @param {number} key
 * @return {void}
 */
MyHashMap.prototype.remove = function(key) {
    this.items[key] = -1;
};

var obj = new MyHashMap();
obj.put(1,1);
var param_2 = obj.get(1);
obj.remove(1);