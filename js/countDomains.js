
function countDomains(cpdomains) {


    resultM = {};
    resultA = [];
    let count = 0;
    let domString = '';
    let domainSplit;
    let tempStr;

    cpdomains.forEach((domain) => {

        domainSplit = domain.split(' ');
        count = parseInt(domainSplit[0]);
        domString = domainSplit[1];

        // while loop here for the real logic
        while (domString.length > 0) {
            if (resultM[domString]) {
                resultM[domString] += count;
            } else {
                resultM[domString] = count;
            }
            if (domString.indexOf('.') == -1) {
                break;
            }
            domString = domString.slice(domString.indexOf('.')+1);
        }

    });

    for (m in resultM) {
        tempStr = resultM[m];
        tempStr += ' ';
        tempStr += m;
        resultA.push(tempStr);
    }
    return resultA;

}



const result = countDomains(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]);
console.log(result);