odoo.define("momo_defi_snippet.animation", function (require) {
    "use strict";

    let sAnimation = require("website.content.snippets.animation");

    sAnimation.registry.demo_website_snippet = sAnimation.Class.extend({
        selector: ".o_momo_defi_snippet",

        start: function () {
            let self = this;
            this._eventList = this.$(".momo_defi_snippet_value");
            this._originalContent = this._eventList.text();
            let def = this._rpc({
                route: "/momo_defi_snippet/defi_aliment",
            }).then(function (data) {
                if (data.error) {
                    return;
                }

                if (_.isEmpty(data)) {
                    return;
                }

                self._$loadedContent = $(data);
                self._eventList.html(data["fruits"].join("<br/>"));
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