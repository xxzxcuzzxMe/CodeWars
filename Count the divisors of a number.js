function getDivisorsCnt(n){
    let nums = 0; 
     for (let i=1; i<=n; i++) {
      if (n % i === 0) {
           nums++; 
   }
   }
     return nums;
   }