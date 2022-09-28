function timeConversion(s) {
  // Write your code here
  let sArr = s.split(":");
  let hr = parseInt(sArr[0]);
  let min = sArr[1];
  let ss = sArr[2].slice(0,2);
  let fmt = sArr[2].slice(-2);
  let newHr = "";
  if(fmt === "PM"){
      if(hr === 12){
          newHr = "12";
      } else { 
          hr = hr + 12;
          newHr = hr.toString();
          }
  } else{
      newHr = hr.toString();
      if(hr<10){
          newHr = "0".concat(hr.toString())
      }
      if(hr === 12){
          newHr = "00";
      }
  }
  let newTime = newHr.concat(":", min, ":", ss);
  return newTime;
  

}