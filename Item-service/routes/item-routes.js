const { getItems, addItem, getItemById } = require('../controllers/item-Controller')


const express = require("express");
const router = express.Router();

router.get("/get-Items", getItems);
router.post("/add-Items", addItem);
router.get("/get-ById:id", getItemById);

module.exports = router;