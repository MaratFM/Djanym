function parse_ajax(data){
	if (data.error){
		alert('Error!\n'+data.error);
		return false;
	}
	if (data.message){
		alert('Message!\n'+data.message);
		return true;
	}	
	return data.data; 
}

jQuery(function($) {

	var div_obj = jQuery('#pages_tree');
	
	div_obj.tree({
		data : { 
			type : "json",
			async : true,
			opts : {
				method : "POST",
				url : async_url
			}
		},
		callback : { 
			
			beforedata : function (n, t) { 
				if(n == false) {
					t.settings.data.opts.static = init_data;
				} else {
					t.settings.data.opts.static = false;
					return { id : jQuery(n).attr("id") };
				}  
			},		
			ondata : function (DATA, TREE_OBJ) {
				if (jQuery.isArray(DATA)) {
					return DATA;
				}else{
					return parse_ajax(DATA);
				}
			},
			onmove : function (NODE, REF_NODE, TYPE, TREE_OBJ,RB) {
				id = NODE.id;
				target = REF_NODE.id;
				if (TYPE=="before"){ position = 'left'; }
				else if (TYPE=="after"){ position = 'right'; }
				else if (TYPE=="inside"){ position = 'last-child'; }
				$.ajax({
      					url: async_url,
      					type: "POST",
      					data: ({id: id, target: target, position: position}),
      					dataType: "json",
      					success: parse_ajax
						})
			}			
		},
		ui : {
			dots: false,
			theme_name : "default"
		},
		plugins : { 
/*			checkbox : { },
			cookie : { prefix : "jstree_", types : {selected: false, open: save_cookies} }
*/		}		
	});


});
