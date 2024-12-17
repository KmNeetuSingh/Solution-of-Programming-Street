function isPalindrome(Str){
    const cleaned = Str.replace(/[^A-Z0-9]/ig, "-").toLowercase;
    return cleaned === Str.split("-").reverse().join("-")
}
console.log(isPalindrome("111"))