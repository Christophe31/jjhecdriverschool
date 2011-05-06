<?php
namespace Jjhec\SafeDriving\Entity

/**
 * @orm:Entity
 */
class Entretient
{
    /**
     * @orm:Id
     * @orm:Column(type="integer")
     * @orm:GeneratedValue(strategy="AUTO")
     */
    protected $id ;

    /**
     * http://symfony.com/doc/2.0/book/doctrine/orm.html
     */
}

// vim:set et sts=4 ts=4 tw=80:
