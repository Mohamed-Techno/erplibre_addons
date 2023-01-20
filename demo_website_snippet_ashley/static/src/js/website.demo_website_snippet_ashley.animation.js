odoo.define("demo_website_snippet_ashley.animation", function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.demo_website_snippet = sAnimation.Class.extend({
        selector: ".o_demo_website_snippet_ashley",

        start: function () {
            let self = this;
            this._eventList = this.$(".demo_website_snippet_ashley_value");
            this._originalContent = this._eventList.text();
            let def = this._rpc({
                route: "/demo_website_snippet_ashley/helloworld",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }
                console.error("error!");
                self._$loadedContent = $(data);
                self._eventList.html(data["fruit"].join("<br/>"));
            });

            return $.when(this._super.apply(this, arguments), def);
        },
        destroy: function () {
            this._super.apply(this, arguments);
            if (this._$loadedContent) {
                this._eventList.text(this._originalContent);
            }
        },
    });
});
