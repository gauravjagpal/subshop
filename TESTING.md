## Testing

Once the program was operational. I began testing for errors.

The deployed project live link [can be accessed here](https://subshop-ceb451619694.herokuapp.com//) - ***Use Ctrl (Cmd) and click to open in a new window.*** 

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Input Type | User is asked what kind of input they want | They proceed to enter item data | Works as expected |
| Input Type | User enters something outside the given list | Loop starts and asks them again | Works as expected |
| Item input | User is asked to enter their item | String entered | Works as expected | 
| Item input | User inputs blank | Error message appears | Works as expected |
| Integer input | User asked to enter minute taken to cook | Move on to next input | Works as expected
| Integer input | Float/blank/string is rejected and asked to re-enter | Error message appears | Works as expected
| Float input | User asked about cost | Move on to next input | Works as expected
| Float input | blank/string is rejected and asked to re-enter | Error message appears | Works as expected


## Testing Browsers
The deployed program was tested in the following browsers:

- Chrome
- Edge
- Firefox
- Oprea
- Safari

It worked without issues in the above browsers.

## Testing Google Sheets
Once the Google Sheets API was connected, I tested various adding items, updating items and deleting items.
When first tested, I was referencing the wrong row through index notation and realised I needed to add a +1 to some elements of code.


### [BACK TO README](README.md)