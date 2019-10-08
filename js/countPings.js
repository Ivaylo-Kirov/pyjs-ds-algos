
class RecentCounter {
    constructor() {
        this.pings = [];
    }

    ping(t) {
        this.pings.push(t);
    
        const result = this.pings.filter((p) => {
            return p >= (t-3000)
        });
        
        this.pings = result;
        return this.pings.length;
    }

}

let rc = new RecentCounter();

rc.ping(1);
rc.ping(100);
rc.ping(3002);
rc.ping(7000);
rc.ping(8000);
rc.ping(13000);