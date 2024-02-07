function fetchJSONData() {
    const sample = require('./templates/data.json');
    console.log(sample[2])
    console.log(sample[2].posx/10)
}
fetchJSONData();