window.onload = function(){
  var l = [["0: McNerney", "https://datastudio.google.com/embed/reporting/0122d2cb-618e-4a41-8d4c-dd2fd505e605/page/dqjgB"], ["1: Amador","https://datastudio.google.com/embed/reporting/451389c1-e692-4dd7-b47b-33983863dce5/page/dqjgB"], ["2: Harder", "https://datastudio.google.com/embed/reporting/0c0a8d40-784f-45dc-baea-41479c86397c/page/dqjgB"], ["3: Howze", "https://datastudio.google.com/embed/reporting/6e53f99b-bb88-4f64-adce-cd690d1dd5d3/page/dqjgB"], ["4: Eggman", "https://datastudio.google.com/embed/reporting/91345be0-44f4-4d18-875d-2b3fca0ef1f4/page/INvfB"], ["5: Ridenour", "https://datastudio.google.com/embed/reporting/6f77ebf6-c195-48f5-82aa-73054e39afa4/page/INvfB"], ["6: Cooper", "https://datastudio.google.com/embed/reporting/04cd4ae9-67b1-4100-8264-5038dd7c7743/page/INvfB"], ["7: Rigard", "https://datastudio.google.com/embed/reporting/0ed82efc-2de9-4ae9-b5ef-46e5eeae31d3/page/INvfB"], ["8: Flora", "https://datastudio.google.com/embed/reporting/e84c38d7-b877-4499-a96f-9ad2dbd5a1b5/page/INvfB"], ["9: Paul Akinjo", ""], ["10: Miller", "https://datastudio.google.com/embed/reporting/13947838-2f5e-445d-aa17-4a171562e743/page/INvfB"], ["11: Villapudua", "https://datastudio.google.com/embed/reporting/ee9af698-91dc-4f54-adf2-e876d6093974/page/INvfB"], ["12: Rhodesia Ransom", "https://datastudio.google.com/embed/reporting/de09fda1-29ee-4ed9-859f-95eb27aae916/page/INvfB"], ["13: Robert Rickman", "https://datastudio.google.com/embed/reporting/f4606ce6-1005-477e-b665-05043d79d1e1/page/INvfB"], ["14: Fritchen", "https://datastudio.google.com/embed/reporting/6f9224e6-cf57-49df-bf5d-a0c9d43252df/page/INvfB"], ["15: Vigil", ""], ["16: Arriola", "https://datastudio.google.com/embed/reporting/47c47266-3293-40eb-8812-f5e55e133828/page/INvfB"], ["17: Young", "https://datastudio.google.com/embed/reporting/0c03ebcf-d5f9-426f-bff1-3cc23a9e0d78/page/INvfB"], ["18: Sangha", "https://datastudio.google.com/embed/reporting/52e39d74-c5f7-4e48-b738-23383cca9377/page/INvfB"], ["19: Wahid", "https://datastudio.google.com/embed/reporting/10976805-658e-4956-b722-98c16970af9d/page/INvfB"], ["20: Bilbrey", "https://datastudio.google.com/embed/reporting/9d5af9a6-6847-4378-9f77-0485c9b3b71a/page/INvfB"], ["21: Tubbs", "https://datastudio.google.com/embed/reporting/db11ff2f-bd8c-4d98-b027-b2c2a3a42ee2/page/INvfB"], ["22: Lincoln", "https://datastudio.google.com/embed/reporting/a6d3f405-0a1d-45a4-b390-b6071f62d3c3/page/INvfB"], ["23: Warmsley", "https://datastudio.google.com/embed/reporting/0cbe917a-1c75-4932-b4c1-9423b46b7053/page/INvfB"], ["24: Allen", "https://datastudio.google.com/embed/reporting/3b54d486-8c32-4634-9960-48171c3aa2c3/page/INvfB"], ["25: Bowman", "https://datastudio.google.com/embed/reporting/2ed20c02-3254-479a-a21e-61c8c111bee8/page/INvfB"], ["26: Mounce", "https://datastudio.google.com/embed/reporting/8488d62d-b5c6-4d41-b5e0-a85329e96f8d/page/INvfB"], ["27: Khan", ""], ["28: Yepez", "https://datastudio.google.com/embed/reporting/4b37cc70-aaa5-4f97-9243-ad18d47b0fe7/page/INvfB"], ["29: Hothi", "https://datastudio.google.com/embed/reporting/82ebadc4-9f19-4ea2-98eb-aba60e8b1f43/page/INvfB"], ["30: Madrigal", "https://datastudio.google.com/embed/reporting/734ef431-13d1-44cf-b0a3-34e04fd9b01c/page/INvfB"], ["31: McKnight", ""], ["32: Singh", "https://datastudio.google.com/embed/reporting/74201aa3-749f-427a-a933-d8905769442f/page/INvfB"], ["33: Moorhead", "https://datastudio.google.com/embed/reporting/148bebf8-22b4-4bb0-a96b-df3589b900b3/page/INvfB"], ["34: Cunha", "https://datastudio.google.com/embed/reporting/9e0bf03d-7fd1-409f-86fd-2df243c951b6/page/INvfB"], ["35: Halford", "https://datastudio.google.com/embed/reporting/5c998687-0c86-4c20-ba16-7e76db968b87/page/INvfB"], ["36: Martin", ""], ["37: Wheeler", "https://datastudio.google.com/embed/reporting/7c0ef7fd-c709-4652-a804-bcd12d89df99/page/INvfB"], ["38: Zuber", ""], ["39: Spade", ""], ["40: Kohl", ""], ["41: deGraaf", ""], ["42: Medina", "https://datastudio.google.com/embed/reporting/660d4636-3671-4b0f-915b-ad610c4e7a2f/page/INvfB"], ["43: Davis", "https://datastudio.google.com/embed/reporting/3edc6ab5-6a4f-4764-8c1e-7e2a7b18c2f3/page/INvfB"], ["44: Wander", "https://datastudio.google.com/embed/reporting/18f58b03-55e5-4842-847c-ada4d4cc7006/page/INvfB"], ["45: Bedolla", "https://datastudio.google.com/embed/reporting/efba0453-452e-4994-8c42-5315a43855a2/page/INvfB"], ["46: Muetzenberg", ""], ["47: Hudson", "https://datastudio.google.com/embed/reporting/94189171-ef19-44b4-87ba-e31d434aa771/page/INvfB"], ["48: Alexander", "https://datastudio.google.com/embed/reporting/c45f1fc8-de08-4c60-abf7-e028e11e54d7/page/INvfB"], ["49: Ortiz", "https://datastudio.google.com/embed/reporting/68c54538-a1c9-4974-953c-b67c63894f10/page/INvfB"], ["50: Mendez", "https://datastudio.google.com/embed/reporting/d5fca58f-baf9-4e4e-b8ab-39735a97c88b/page/INvfB"], ["51: Shackelford", "https://datastudio.google.com/embed/reporting/a3bdbf93-8782-41e3-a604-9974c86aae64/page/INvfB"], ["52: Barrett", ""], ["53: Silva",  "https://datastudio.google.com/embed/reporting/3fc86b8c-eabe-4ea0-8dad-4dae5810f705/page/INvfB"], ["54: Jones", ""], ["55: Rico", "https://datastudio.google.com/embed/reporting/62e1871e-76e1-4ab7-9f4a-9fe2246d89f8/page/INvfB"], ["56: Silva", ""], ["57: Silva", ""], ["58: Barbosa", ""], ["59: Duncan", ""], ["60: Pearsall", ""], ["61: Greene", "https://datastudio.google.com/embed/reporting/76239360-46ba-4f80-842f-d936f8718087/page/INvfB"], ["62: Morowit", "https://datastudio.google.com/embed/reporting/b66378cc-a5bf-4e9e-80eb-2ce87bf301eb/page/INvfB"], ["63: Wallace", ""], ["64: CampoyLauglin", ""], ["65: Guerrero", ""], ["66: To-Cowell", "https://datastudio.google.com/embed/reporting/54d3cf06-18be-4342-bf63-e3ba6928bb87/page/INvfB"], ["67: Blanchard", "https://datastudio.google.com/embed/reporting/4b9485b8-3bb6-4f79-86ea-31ae2b0069e2/page/INvfB"], ["68: Flores", ""], ["69: Castellanos", "https://datastudio.google.com/embed/reporting/f82d8802-ac6d-4c3f-ad6f-7014536a8bee/page/INvfB"], ["70: Garcia", ""], ["71: Giudici", ""], ["72: Brown", "https://datastudio.google.com/embed/reporting/abfcdfbf-0de7-4481-9e5c-3b639fb1fc90/page/INvfB"], ["73: Goodall", "https://datastudio.google.com/embed/reporting/18dd2d07-3265-460f-9f7c-452e2db7a00a/page/INvfB"], ["74: Knackstedt", ""], ["75: Vasquez", ""], ["76: Freitas", "https://datastudio.google.com/embed/reporting/b5930960-7a79-4cbc-a8ca-3eb85171d1ba/page/INvfB"], ["77: Pack", ""], ["78: JosephPrice", ""], ["79: Nava", ""], ["80: Troy", ""], ["81: Mitchell", ""], ["82: Marable", ""], ["83: Jeffs", "https://datastudio.google.com/embed/reporting/34bfd964-73c6-42c2-9764-2ed0e22c13d8/page/INvfB"], ["84: Erskine", ""], ["85: Hoffert", ""], ["86: Costa", ""], ["87: Silcox", ""], ["88: Blanco", ""], ["89: Mann", ""], ["90: Chan", "https://datastudio.google.com/embed/reporting/e27c5ddc-9b4f-497a-91e5-318e86582fe7/page/INvfB"], ["91: Antonini", ""], ["92: Jones", ""], ["93: Frazier", ""], ["94: Pombo", ""], ["95: Olsen", ""], ["96: Bonilla", ""], ["97: Cornelious", ""], ["98: Dhillon", "https://datastudio.google.com/embed/reporting/e4e19e4b-24b1-42cf-b629-537ece7ffbfb/page/INvfB"], ["99: Su", ""], ["100: Harrison", ""], ["101: KingTingle", ""], ["98: Dhillon", "https://datastudio.google.com/embed/reporting/e4e19e4b-24b1-42cf-b629-537ece7ffbfb/page/INvfB"], ["99: Su", ""], ["100: Harrison", ""], ["101: KingTingle", ""], ["102: A", ""], ["103: Malapaka", ""], ["104: Liew", ""], ["105: Luntao", "https://datastudio.google.com/embed/reporting/6f9f2d99-5f8b-4f05-a5b7-4343ba907758/page/INvfB"], ["106: Casillas", ""], ["107: Zulueta", ""]];
  if (window.innerWidth <= 667){
    document.getElementsByTagName("iframe")[0].src = l[document.getElementById("linknum").content][1];
  }
};
