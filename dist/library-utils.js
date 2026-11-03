function parseLibraryFile(text,allowedIds){
 if(typeof text!=='string'||text.length>1000000)throw new Error('O arquivo é grande demais. Use uma exportação do NOVA PLAY.');
 let data;try{data=JSON.parse(text)}catch{throw new Error('O arquivo não é um JSON válido. Escolha uma exportação do NOVA PLAY.');}
 if(!data||data.format!=='nova-play-library'||data.version!==1||!Array.isArray(data.favorites)||!Array.isArray(data.recent))throw new Error('Formato inválido. Escolha um arquivo exportado pelo NOVA PLAY.');
 const allowed=new Set(allowedIds),clean=a=>[...new Set(a.filter(x=>typeof x==='string'&&allowed.has(x)))];
 return {favorites:clean(data.favorites),recent:clean(data.recent).slice(0,40)};
}
