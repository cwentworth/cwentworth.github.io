var sfActs = acts.filter(val => {
return val.scw === 'hotdog';
});
};
var mdcn = sfActs.filter(function (x) {return x.type == 'medication';});
var szr = sfActs.filter(function (x) {return x.type == 'seizure';});

var mxMdcnDt = Math.max.apply(Math, mdcn.map(function(o) { return o.dt; }));
var mxSzrDt = Math.max.apply(Math, szr.map(function(o) { return o.dt; }));

Date.prototype.addHours = function(h) {
   this.setTime(this.getTime() + (h*60*60*1000));
   return this;
};

var cT = Date.now();
var mxMdcnDtForm = new Date(mxMdcnDt);
var MdcnDue = mxMdcnDtForm.addHours(12);
var MdcnDue_raw = MdcnDue.getTime();

var deltMdcn_raw = Math.abs(cT - mxMdcnDt) / 1000;
var deltMdcn_s = deltMdcn_raw % 60;
var deltMdcn_m = Math.floor(deltMdcn_raw / 60) % 60;
var deltMdcn_h = Math.floor(deltMdcn_raw / 3600) % 24;
var deltMdcn_d = Math.floor(deltMdcn_raw / 86400);

var MdcnDue_raw_r = Math.abs(MdcnDue_raw - cT) / 1000;
var MdcnDue_s = MdcnDue_raw_r % 60;
var MdcnDue_m = Math.floor(MdcnDue_raw_r / 60) % 60;
var MdcnDue_h = Math.floor(MdcnDue_raw_r / 3600) % 24;


var MdcnStmnt = 'It has been '
+ deltMdcn_h + ' hour(s) and '
+ deltMdcn_m + ' minute(s) since Lulu last had her medication.';

if(MdcnDue_h < 1) {
var MdcnInstructions = "Lulu's next dose is needed in about " + MdcnDue_m + " minute(s)";
};

if(MdcnDue_h >= 1) {
var MdcnInstructions = "Lulu's next dose is needed in about " + MdcnDue_h + " hour(s)";
};

var deltSzr_raw = Math.abs(cT - mxSzrDt) / 1000;
var deltSzr_s = deltSzr_raw % 60;
var deltSzr_m = Math.floor(deltSzr_raw / 60) % 60;
var deltSzr_h = Math.floor(deltSzr_raw / 3600) % 24;
var deltSzr_d = Math.floor(deltSzr_raw / 86400);

var SzrStmnt = 'It has been '
+ deltSzr_d + ' day(s) '
+ deltSzr_h + ' hour(s) and '
+ deltSzr_m + ' minute(s) since Lulu last had a seizure.';
