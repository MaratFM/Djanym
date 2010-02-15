$(document).ready(function() {
    if (!$('#tree').length)
        return false;

    $(function() {
        window.jtree = $("#tree").tree({
            /*ui: {
                theme_name: 'apple'
            },*/

            plugins: {
                contextmenu: {
                    items: {
                        remove: true,
                        create: {
                            label: "Create",
                            icon: "create",
                            visible: function(node, treeobj) {
                                if (node.length != 1)
                                    return 0;
                                return treeobj.check("creatable", node);
                            },
                            action: function(node, treeobj) {
                                location.href = 'add/?parent=' + node.attr('id').replace('n','');
                                },
                            separator_after: true
                        },
                        rename: {
                            label: "Rename",
                            icon: "rename",
                            visible: function(node, treeobj) {
                                if (node.length != 1)
                                    return false;
                                return treeobj.check("renameable", node);
                            },
                            action: function(node, treeobj) {
                                treeobj.rename(node);
                            }
                        },
                        edit: {
                            label: "Change",
                            icon: "rename",
                            visible: function(node, treeobj) {
                                if (node.length != 1)
                                    return false;
                                return true;
                            },
                            action: function(node, treeobj) {
                                location.href = $(node).attr('id').replace('n','') + '/';
                            }
                        },
                        remove: {
                            label: "Remove",
                            icon: "remove",
                            visible: function(node, treeobj) {
                                if (node.length != 1)
                                    return false;
                                return treeobj.check("deletable", node);
                            },
                            action: function(node, treeobj) {

                                treeobj.remove(node);
                                
                            }
                        }

                    }
                }

            },

            callback: {
                /*onmove: function(node, ref_node, TYPE, treeobj, RB) {

                },*/
                beforemove: function(node, ref_node, TYPE, treeobj) {
                    if(treeobj._moving){
                        treeobj._moving=false;
                        return true;
                    }else treeobj._moving=true;
                    var position={'inside':'last-child','before':'left','after':'right'}[TYPE];
                    treeobj.settings.data.opts.url = 'move_node/';
                    treeobj.settings.data.opts.method='POST';
                    treeobj._params={node:node.id.replace('n',''),target:ref_node.id.replace('n',''),position:position};
                    treeobj.refresh();
                    /*$.ajax({url:'move_node/',type:'POST',success: function(data) {
                    //$.tree.reference(window.jtree).refresh();
                        treeobj.refresh();
                        //treeobj.moved($(node),$(ref_node).children("ul:eq(0)").children("li:last").children("a:eq(0)"),TYPE);
                    },data: ({node:node.id.replace('n',''),target:ref_node.id.replace('n',''),
                    position:position})
                    });*/
                    return false;
                },
                ondblclk: function(node, treeobj) {
                    location.href = $(node).attr('id').replace('n','');
                },
                onload: function(treeobj) {
                    treeobj.open_all();
                },
                onrename: function(node, treeobj, RB) {
                    //treeobj.settings.data._node=node;
                    var new_name=$(node).children('a:first').text();//.replace(/^\s\s*/, '');
                    treeobj._params={node:node.id.replace('n',''),name:new_name};
                    treeobj.settings.data.opts.url = 'rename/';
                    treeobj.settings.data.opts.method = 'POST';
                    treeobj.refresh();
                    /*$.ajax({url:'rename/',type:'POST',success:
                            function(data) {
                                treeobj.rename(RB,new_name);
                        //$.tree.reference(window.jtree).refresh();
                        },
                    data: ({node:node.id.replace('n',''),name:new_name})
                    });*/
                    return false;
                },
                beforedelete: function(node, treeobj) {
                    treeobj._params={node:node.id.replace('n','')};
                    treeobj.settings.data.opts.url = 'remove/';
                    treeobj.settings.data.opts.method = 'POST';
                    treeobj.refresh();
                    /*$.ajax({url:'remove/',type:'POST',success:
                        function(data) {
                        //$.tree.reference(window.jtree).refresh();
                        //$.tree.reference(window.jtree).refresh();
                        treeobj.remove(node);
                        //treeobj.refresh();
                        },data: ({node:node.id.replace('n','')})
                    });*/
                    return false;
                },
                onsearch : function (n,t) {
		    t.container.find('.search').removeClass('search');
		    n.addClass('search');
		},
                ondata: function(data, treeobj) {
                    if(typeof(treeobj._params)!='undefined'){
                    treeobj._params={};
                    treeobj.settings.data.opts.url='tree/';
                    treeobj.settings.data.opts.method='POST';}
                    return data;
                },
                beforedata: function(node, treeobj) {
                    return typeof(treeobj._params)!='undefined' && treeobj._params || {};
                },
                onchange : function (node) {
                    document.location.href = $(node).children("a:eq(0)").attr("href");
                }

            },
            data: {
                type: "html",async: false
                //opts : { method: "POST", url: "tree/" }
            },
            "types": {
                "default": permissions
            }
        });
    });
    //jQuery.tree.reference('#tree')._params={};
    $('#changelist').removeClass('module');

});

