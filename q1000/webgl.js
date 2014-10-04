function base64ToUint8Array( base64 ) {
    var raw = window.atob(base64);
    var rawLength = raw.length;
    var u8_array = new Uint8Array(new ArrayBuffer(rawLength));
	 
    for(i = 0; i < rawLength; i++) {
    	u8_array[i] = raw.charCodeAt(i);
    }
    return u8_array;
}
